#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    def print_values(
        cpu="Intel",
        ram=16,
        disk="SSD",
        video="NVIDIA",
                    ):
        print(f"Процессор  {cpu}")
        print(f"Память     {ram}Gb")
        print(f"Накопитель {disk}")
        print(f"Видео      {video}")

print('все значения по умолчанию')
print_values()

newPC1 = {"cpu": "AMD"}
print('изменяем процессор для PC1')
print_values(**newPC1)

newPC2 = {"video": "Radeon", "ram": 64}
print('изменяем видеокарту и память для PC2')
print_values(**newPC2)

newPC3 = {"cpu": "Ryzen", "ram": 128}
print('изменяем процессор и память для PC2')
print_values(**newPC3)
