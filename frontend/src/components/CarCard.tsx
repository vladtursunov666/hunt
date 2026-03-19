import { Car } from '../lib/types';

const statusLabel: Record<string, string> = {
  overpriced_high: 'Сильно выше рынка',
  overpriced: 'Выше рынка',
  market: 'По рынку',
  underpriced: 'Ниже рынка',
  underpriced_high: 'Сильно ниже рынка',
};

export function CarCard({ car, onSelect, onFavorite }: { car: Car; onSelect: (id: number) => void; onFavorite: (id: number) => void }) {
  return (
    <article className="card">
      <img className="card__image" src={car.image_url} alt={`${car.brand} ${car.model}`} />
      <div className="card__body">
        <div className="card__header">
          <div>
            <h3>{car.brand} {car.model}</h3>
            <p>{car.year} • {car.mileage.toLocaleString('ru-RU')} км • {car.region}</p>
          </div>
          {car.premium_only && <span className="badge badge--premium">Premium</span>}
        </div>
        <div className="card__metrics">
          <div>
            <span>Цена лота</span>
            <strong>{car.price.toLocaleString('ru-RU')} ₽</strong>
          </div>
          <div>
            <span>Средний рынок</span>
            <strong>{car.average_price.toLocaleString('ru-RU')} ₽</strong>
          </div>
          <div>
            <span>Отклонение</span>
            <strong className={`status status--${car.status}`}>{car.deviation_percent}%</strong>
          </div>
        </div>
        <div className="card__footer">
          <span className={`pill pill--${car.status}`}>{statusLabel[car.status]}</span>
          <div className="card__actions">
            <button onClick={() => onSelect(car.id)}>Подробнее</button>
            <button className="button-secondary" onClick={() => onFavorite(car.id)}>В избранное</button>
          </div>
        </div>
      </div>
    </article>
  );
}
