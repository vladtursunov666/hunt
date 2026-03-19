import { CarDetail as CarDetailType } from '../lib/types';

const statusLabel: Record<string, string> = {
  overpriced_high: 'Сильно выше рынка',
  overpriced: 'Выше рынка',
  market: 'По рынку',
  underpriced: 'Ниже рынка',
  underpriced_high: 'Сильно ниже рынка',
};

export function CarDetail({ car, onBack }: { car: CarDetailType; onBack: () => void }) {
  return (
    <section className="detail">
      <button className="button-secondary" onClick={onBack}>← К списку</button>
      <div className="detail__hero">
        <img src={car.image_url} alt={`${car.brand} ${car.model}`} />
        <div>
          <h2>{car.brand} {car.model}</h2>
          <p>{car.year} • {car.mileage.toLocaleString('ru-RU')} км • {car.region}</p>
          <div className="detail__stats">
            <div><span>Цена лота</span><strong>{car.price.toLocaleString('ru-RU')} ₽</strong></div>
            <div><span>Средний рынок</span><strong>{car.average_price.toLocaleString('ru-RU')} ₽</strong></div>
            <div><span>Статус</span><strong className={`status status--${car.status}`}>{statusLabel[car.status]}</strong></div>
          </div>
          <a className="detail__cta" href={car.url} target="_blank" rel="noreferrer">Открыть торги</a>
        </div>
      </div>

      <div className="detail__comparables">
        <h3>Рыночные аналоги</h3>
        <table>
          <thead>
            <tr>
              <th>Объявление</th>
              <th>Год</th>
              <th>Пробег</th>
              <th>Цена</th>
            </tr>
          </thead>
          <tbody>
            {car.comparables.map((item) => (
              <tr key={item.id}>
                <td><a href={item.url} target="_blank" rel="noreferrer">{item.title}</a></td>
                <td>{item.year}</td>
                <td>{item.mileage.toLocaleString('ru-RU')} км</td>
                <td>{item.price.toLocaleString('ru-RU')} ₽</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
