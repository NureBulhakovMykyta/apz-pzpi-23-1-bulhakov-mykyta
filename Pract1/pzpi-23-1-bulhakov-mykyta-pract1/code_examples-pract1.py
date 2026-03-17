from abc import ABC, abstractmethod

# ==========================================================
# 1. ПОЧАТКОВА РЕАЛІЗАЦІЯ (Проблема: порушення принципів SOLID)
# ==========================================================

class NavigatorLegacy:
    """
    Клас має забагато відповідальностей та важко розширюється.
    При додаванні нового виду транспорту доводиться змінювати основний клас.
    """
    def build_route(self, start, destination, transport_type):
        if transport_type == "CAR":
            print("Будуємо маршрут для автомобіля...")
            return self._calculate_car_route(start, destination)
        elif transport_type == "WALKING":
            print("Будуємо маршрут для пішохода...")
            return self._calculate_walking_route(start, destination)
        elif transport_type == "PUBLIC_TRANSPORT":
            print("Будуємо маршрут для громадського транспорту...")
            return self._calculate_transit_route(start, destination)
        elif transport_type == "BICYCLE":
            print("Будуємо маршрут для велосипеда...")
            return self._calculate_bicycle_route(start, destination)
        else:
            raise ValueError(f"Невідомий тип транспорту: {transport_type}")

    def _calculate_car_route(self, start, destination):
        return f"Авто-маршрут: {start} -> {destination}"

    def _calculate_walking_route(self, start, destination):
        return f"Піший маршрут: {start} -> {destination}"

    def _calculate_transit_route(self, start, destination):
        pass

    def _calculate_bicycle_route(self, start, destination):
        pass


# ==========================================================
# 2. ОПТИМІЗОВАНА РЕАЛІЗАЦІЯ (Паттерн Strategy)
# ==========================================================

# Спільний інтерфейс для всіх стратегій
class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, start, destination):
        pass

# Конкретні стратегії (алгоритми)
class CarStrategy(RouteStrategy):
    def build_route(self, start, destination):
        print("Будуємо маршрут для автомобіля...")
        return f"Автомобільний маршрут: {start} -> {destination}"

class WalkingStrategy(RouteStrategy):
    def build_route(self, start, destination):
        print("Будуємо маршрут для пішохода...")
        return f"Пішохідний маршрут: {start} -> {destination}"

class PublicTransportStrategy(RouteStrategy):
    def build_route(self, start, destination):
        print("Будуємо маршрут для громадського транспорту...")
        return f"Маршрут транспортом: {start} -> {destination}"

# Контекст: використовує стратегії незалежно від їхньої внутрішньої логіки
class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        self._strategy = strategy

    def build_route(self, start, destination):
        # Делегування виконання алгоритму обраній стратегії
        result = self._strategy.build_route(start, destination)
        print(result)
        return result


# ==========================================================
# 3. ДЕМОНСТРАЦІЯ РОБОТИ
# ==========================================================

if __name__ == "__main__":
    start_point = "Київ, Майдан"
    end_point = "Київ, Подол"

    print("--- Використання паттерну Strategy ---")
    
    # Створюємо навігатор з початковою стратегією (Авто)
    navigator = Navigator(CarStrategy())
    navigator.build_route(start_point, end_point)

    # Динамічна зміна поведінки під час виконання програми
    print("\nЗмінюємо стратегію на пішохідну...")
    navigator.set_strategy(WalkingStrategy())
    navigator.build_route(start_point, end_point)

