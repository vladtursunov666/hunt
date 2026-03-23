import { Car } from '../lib/types';

export function CarCard({ car }: { car: Car }) {
  return (
    <article className="card card--simple">
      <div className="card__body">
        <h2 className="card__title">{car.brand} {car.model}</h2>
        <ul className="card__list">
          <li>
            <span>Марка</span>
            <strong>{car.brand}</strong>
          </li>
          <li>
            <span>Модель</span>
            <strong>{car.model}</strong>
          </li>
          <li>
            <span>Цена лота</span>
            <strong>{car.price.toLocaleString('ru-RU')} ₽</strong>
          </li>
          <li>
            <span>Средняя цена</span>
            <strong>{car.average_price.toLocaleString('ru-RU')} ₽</strong>
          </li>
          <li>
            <span>Процент отклонения</span>
            <strong className="card__deviation">{car.deviation_percent}%</strong>
          </li>
        </ul>
      </div>
    </article>
  );
}
