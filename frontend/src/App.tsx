import { useEffect, useMemo, useState } from 'react';
import { CarCard } from './components/CarCard';
import { CarDetail } from './components/CarDetail';
import { Filters, FiltersState } from './components/Filters';
import { addFavorite, fetchCar, fetchCars, fetchFavorites } from './lib/api';
import { Car, CarDetail as CarDetailType } from './lib/types';

declare global {
  interface Window {
    Telegram?: {
      WebApp?: {
        ready: () => void;
        expand: () => void;
        initDataUnsafe?: {
          user?: { id?: number; first_name?: string };
        };
      };
    };
  }
}

const initialFilters: FiltersState = {
  brand: '',
  region: '',
  year: '',
  price_min: '',
  price_max: '',
  deviation_min: '',
  deviation_max: '',
  only_free: false,
};

export default function App() {
  const [cars, setCars] = useState<Car[]>([]);
  const [filters, setFilters] = useState<FiltersState>(initialFilters);
  const [selectedCar, setSelectedCar] = useState<CarDetailType | null>(null);
  const [favorites, setFavorites] = useState<number[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const telegramId = window.Telegram?.WebApp?.initDataUnsafe?.user?.id ?? 777000;
  const userName = window.Telegram?.WebApp?.initDataUnsafe?.user?.first_name ?? 'Гость';

  useEffect(() => {
    window.Telegram?.WebApp?.ready();
    window.Telegram?.WebApp?.expand();
  }, []);

  const queryParams = useMemo(() => {
    const entries = Object.entries(filters).filter(([, value]) => value !== '' && value !== false);
    return Object.fromEntries(entries.map(([key, value]) => [key, String(value)]));
  }, [filters]);

  useEffect(() => {
    async function load() {
      try {
        setLoading(true);
        const [carsResponse, favoriteResponse] = await Promise.all([
          fetchCars(queryParams),
          fetchFavorites(telegramId),
        ]);
        setCars(carsResponse.items);
        setFavorites(favoriteResponse.map((item: { car: Car }) => item.car.id));
        setError(null);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Неизвестная ошибка');
      } finally {
        setLoading(false);
      }
    }
    void load();
  }, [queryParams, telegramId]);

  async function openCar(id: number) {
    try {
      const car = await fetchCar(id);
      setSelectedCar(car);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Не удалось открыть карточку');
    }
  }

  async function saveFavorite(id: number) {
    try {
      await addFavorite(telegramId, id);
      if (!favorites.includes(id)) {
        setFavorites([...favorites, id]);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Не удалось сохранить избранное');
    }
  }

  return (
    <main className="app-shell">
      <header className="hero">
        <div>
          <p className="eyebrow">Telegram Mini App</p>
          <h1>Hunt Auto</h1>
          <p>Привет, {userName}. Аналитика авто-банкротов: реальная цена лота, средний рынок и отклонение в %.</p>
        </div>
        <div className="hero__stats">
          <div><strong>{cars.length}</strong><span>лотов в выдаче</span></div>
          <div><strong>{favorites.length}</strong><span>в избранном</span></div>
        </div>
      </header>

      {selectedCar ? (
        <CarDetail car={selectedCar} onBack={() => setSelectedCar(null)} />
      ) : (
        <>
          <Filters value={filters} onChange={setFilters} />
          {error && <div className="alert">{error}</div>}
          {loading ? (
            <div className="loading">Загружаем лоты и аналитику…</div>
          ) : (
            <section className="cards">
              {cars.map((car) => (
                <div key={car.id} className="cards__item">
                  <CarCard car={car} onSelect={openCar} onFavorite={saveFavorite} />
                  {favorites.includes(car.id) && <span className="saved-note">★ Уже в избранном</span>}
                </div>
              ))}
            </section>
          )}
        </>
      )}
    </main>
  );
}
