from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap_year(year: int) -> bool:
        #año bisiesto: divisible entre 4 y 400 y no divisible entre 100

        resultado = False
        
        if year % 4 == 0 and year % 100 != 0:
            resultado = True
        elif year % 400 == 0:
            resultado = True

        return resultado

        #Otra opción es:  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    @staticmethod
    def days_in_month( month: int, year: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Date.is_leap_year(year) and month == 2:
            return 29
        else:
            return days[month - 1]

    def get_delta_days(self, day: int, month: int, year: int) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        diaInicial = 1
        mesInicial = 1
        anoInicial = 1900
        diaActual = day
        mesActual = month
        anoActual = year
        diasTranscurridos = 0
      
        while anoInicial < anoActual:
            diasTranscurridos += 365
            if Date.is_leap_year(anoInicial):
                diasTranscurridos += 1
            anoInicial += 1

        while mesInicial < mesActual:
            diasTranscurridos += Date.days_in_month(mesInicial, anoInicial)
            mesInicial += 1

        diasTranscurridos += (diaActual - diaInicial)
        return diasTranscurridos

    @property
    def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        diaSemana = (self.get_delta_days(self.day, self.month, self.year) + 1) % 7
        return diaSemana

    @property
    def is_weekend(self) -> bool:
        ...

    @property
    def short_date(self) -> str:
        '''02/09/2003'''
        ...

    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        ...

    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        ...

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        ...

    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...

    def __eq__(self, other) -> bool:
        ...



uno = Date(7, 4, 2024)
print(uno.get_delta_days(2, 4, 2024))
print(uno.weekday)
    