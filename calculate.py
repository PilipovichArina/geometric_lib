import circle 
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
''' Вычисляет заданную функцию (периметр или площадь) для указанной фигуры (круг или квадрат)
    на основе переданных размеров и выводит результат на экран.

    Параметры:
    fig (str): Название фигуры, для которой будет выполняться расчет. 
               Должно быть одним из значений в списке figs (доступные фигуры: 'circle', 'square').
    
    func (str): Название функции, которую необходимо выполнить. 
                Должно быть одним из значений в списке funcs (доступные функции: 'perimeter', 'area').

    size (list): Список размеров, необходимых для вычисления функции. 
                 Размеры передаются как аргументы в соответствующую функцию из модуля circle или square.
                 Например, для круга это может быть радиус, а для квадрата — длина стороны.

    Результат:
    Выводит строку в формате '{func} of {fig} is {result}', где result — это результат вычисления 
    заданной функции для указанной фигуры с использованием переданных размеров. '''

	''' Проверяем, что указанная фигура доступна ''' 
	assert fig in figs
	'''' Проверяем, что указанная функция доступна '''
	assert func in funcs
	''' Вычисляем результат с помощью динамического вызова функции '''
	result = eval(f'{fig}.{func}(*{size})')
	''' Выводим результат на экран '''
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



