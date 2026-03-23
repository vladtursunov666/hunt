import { CarCard } from './components/CarCard';
import { mockCars } from './data.mockCars';

export default function App() {
  return (
    <main className="app-shell">
      <header className="hero">
        <div>
          <p className="eyebrow">Главная страница</p>
          <h1>Список автомобилей</h1>
          <p>Ниже отображаются 5 тестовых автомобилей с ценой лота, средней ценой по рынку и процентом отклонения.</p>
        </div>
        <div className="hero__stats">
          <div>
            <strong>{mockCars.length}</strong>
            <span>тестовых авто</span>
          </div>
        </div>
      </header>

      <section className="cards">
        {mockCars.map((car) => (
          <CarCard key={car.id} car={car} />
        ))}
      </section>
    </main>
  );
}
