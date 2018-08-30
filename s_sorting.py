import cx_Oracle
from main import *
import datetime

start = datetime.datetime.now()

# game([1, 3, 5, 7, 4, 6, 2], 2)
# game(to_tuple('4 3 2 1'), 2)

# print_situation(generate_begining_situation([1, 2, 3], 5), 5)
# print(generate_agenda(6))
# for i in range(5, 0, -1):
#     print(i)

sit = generate_beginning_layout([1, 2, 3, 4, 5, 6], 2)
print_layout(sit, 2)
print_layout(fix_values(sit, 4), 2)

end = datetime.datetime.now()
elapsed = end - start
print(elapsed.seconds // 60, ' min ', elapsed.seconds % 60, " sec ", elapsed.microseconds, ' microsec')













#  TODO: expected runtime 2 hrs
# magic = input('enter password for database')
# con = cx_Oracle.connect('system/{}@localhost/xe'.format(magic))
# magic = ''
# cur = con.cursor()
# cur1 = con.cursor()
#
# cur.execute('select permutation_ID, permutation from PERMUTATIONS_9 where EVEN_BASIC is null AND ODD_BASIC is null')
# x = 0
# for result in cur:
#     x = x + 1
#     new_odd = odd_basic(to_tuple(result[1]))
#     if new_odd:
#         stmt = "update permutations_9 set odd_basic = '{}', odd_basic_size = {} where permutation_ID = {}"\
#             .format(to_string(new_odd), str(int((len(to_string(new_odd)) + 1)/2)), str(result[0]))
#         cur1.execute(stmt)
#         print(stmt)
#     new_even = even_basic(to_tuple(result[1]))
#     if new_even:
#         stmt = "update permutations_9 set even_basic = '{}', even_basic_size = {} where permutation_ID = {}"\
#             .format(to_string(new_even), str(int((len(to_string(new_even)) + 1) / 2)), str(result[0]))
#         cur1.execute(stmt)
#         print(stmt)
#     cur1.execute('commit')
#     print(x)
# cur.close()
# con.close()
#
# end = datetime.datetime.now()
# elapsed = end - start
# print(elapsed.seconds // 60, ' min ', elapsed.seconds % 60, " sec ", elapsed.microseconds, ' microsec')
