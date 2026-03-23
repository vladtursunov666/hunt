export type FiltersState = {
  brand: string;
  region: string;
  year: string;
  price_min: string;
  price_max: string;
  deviation_min: string;
  deviation_max: string;
  only_free: boolean;
};

export function Filters({ value, onChange }: { value: FiltersState; onChange: (next: FiltersState) => void }) {
  return (
    <section className="filters">
      <h2>Фильтры</h2>
      <div className="filters__grid">
        <input placeholder="Марка" value={value.brand} onChange={(e) => onChange({ ...value, brand: e.target.value })} />
        <input placeholder="Регион" value={value.region} onChange={(e) => onChange({ ...value, region: e.target.value })} />
        <input placeholder="Год" value={value.year} onChange={(e) => onChange({ ...value, year: e.target.value })} />
        <input placeholder="Цена от" value={value.price_min} onChange={(e) => onChange({ ...value, price_min: e.target.value })} />
        <input placeholder="Цена до" value={value.price_max} onChange={(e) => onChange({ ...value, price_max: e.target.value })} />
        <input placeholder="% отклонения от" value={value.deviation_min} onChange={(e) => onChange({ ...value, deviation_min: e.target.value })} />
        <input placeholder="% отклонения до" value={value.deviation_max} onChange={(e) => onChange({ ...value, deviation_max: e.target.value })} />
        <label className="checkbox">
          <input type="checkbox" checked={value.only_free} onChange={(e) => onChange({ ...value, only_free: e.target.checked })} />
          Только бесплатные лоты
        </label>
      </div>
    </section>
  );
}
