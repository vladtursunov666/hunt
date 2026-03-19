export type Car = {
  id: number;
  brand: string;
  model: string;
  year: number;
  mileage: number;
  price: number;
  average_price: number;
  deviation_percent: number;
  status: string;
  region: string;
  url: string;
  image_url: string;
  premium_only: boolean;
};

export type CarDetail = Car & {
  source_name: string;
  comparables: Array<{
    id: number;
    source_name: string;
    title: string;
    year: number;
    mileage: number;
    price: number;
    url: string;
  }>;
};

export type CarsResponse = {
  items: Car[];
  total: number;
};
