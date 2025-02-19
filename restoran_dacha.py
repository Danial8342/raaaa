import menu
import advice

name = input('Доброго дня, як мені до вас звертатися:')
print('Доброго дня' + ' ' + name)
suma = 0
chek = ''

portions_of_breakfast_bufet_for_little_ones = int(
    input('раджу замовити ' + advice.ADVICE_FOR_BREAKFAST_BUFET_FOR_LITTLE_ONES + ' ' + 'скільки порцій хочете?'))
suma = suma + portions_of_breakfast_bufet_for_little_ones * menu.BREAKFAST_BUFET_FOR_LITTLE_ONES
chek = chek + 'BREAKFAST_BUFET_FOR_LITTLE_ONES ' + str(portions_of_breakfast_bufet_for_little_ones) + ' штук по ' + str(
    menu.BREAKFAST_BUFET_FOR_LITTLE_ONES) + 'грн\n'

lazy_dumplings_with_strawberries_and_honey = int(input(
    'можу ще порадити ' + advice.ADVICE_FOR_LAZY_DUMPLINGS_WITH_STRAWBERRIES_AND_HONEY + ', ' + 'скільки порцій хочете?'))
chek = chek + 'ADVICE_FOR_LAZY_DUMPLINGS_WITH_STRAWBERRIES_AND_HONEY ' + str(
    lazy_dumplings_with_strawberries_and_honey) + ' штук по ' + str(
    menu.TENDER_DUMPLINGS_MADE_FROM_CHEESE_DOUGH_BOILED_AND_SERVED_WITH_FRESH_STRAWBERRIES) + 'грн\n'
suma = suma + lazy_dumplings_with_strawberries_and_honey * menu.TENDER_DUMPLINGS_MADE_FROM_CHEESE_DOUGH_BOILED_AND_SERVED_WITH_FRESH_STRAWBERRIES

print('з вас\n==================================')
print(str(suma) + ' грн')

print('сьогодні у нас в ресторані супер акція - всім клієнтам знижка 15%')
suma = suma - (suma * 0.15)
print('check\n==================================')
print(chek + '\n==================================')
print(str(suma) + ' грн')
