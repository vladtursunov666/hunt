import { CarDetail, CarsResponse } from './types';

const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000';

export async function fetchCars(params: Record<string, string>) {
  const search = new URLSearchParams(params);
  const response = await fetch(`${API_URL}/cars?${search.toString()}`);
  if (!response.ok) {
    throw new Error('Не удалось загрузить список автомобилей');
  }
  return (await response.json()) as CarsResponse;
}

export async function fetchCar(id: number) {
  const response = await fetch(`${API_URL}/cars/${id}`);
  if (!response.ok) {
    throw new Error('Не удалось загрузить карточку автомобиля');
  }
  return (await response.json()) as CarDetail;
}

export async function addFavorite(telegramId: number, carId: number) {
  const response = await fetch(`${API_URL}/favorite`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ telegram_id: telegramId, car_id: carId }),
  });
  if (!response.ok) {
    throw new Error('Не удалось добавить в избранное');
  }
  return response.json();
}

export async function fetchFavorites(telegramId: number) {
  const response = await fetch(`${API_URL}/users/${telegramId}/favorites`);
  if (!response.ok) {
    throw new Error('Не удалось загрузить избранное');
  }
  return response.json();
}
