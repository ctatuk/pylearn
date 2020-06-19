from collections import defaultdict

def sales(list_s):
    sales_result = defaultdict(lambda: defaultdict(int))
    for a, b, c in list_s:
        sales_result[a][b] += c
    print(sales_result)
        
        
def sales2(list):
    sales_result = {}  # create new dictionary
    for n, m, k in list:
        if n in sales_result.keys():
            tmp = sales_result.pop(n) + (m, k)
            print(tmp)
            sales_result[n] = tmp
        else:
            sales_result[n] = (m, k)
    print("1", sales_result)
    sort_sales = sorted(sales_result.items())
    # for i, j in sort_sales
    print(2,sort_sales)
    for row in sort_sales:
        print(row)

sales2([('Ivanov', 'paper', 10), ('Petrov', 'pens', 5), ('Ivanov', 'marker', 3),
       ('Ivanov', 'paper', 7), ('Petrov', 'envelope', 20), ('Ivanov', 'envelope', 5)])


sales2([('Alex', 'paper', 10), ('Petrov', 'pens', 5), ('Alex', 'marker', 3),
       ('Alex', 'paper', 7), ('Petrov', 'envelope', 20), ('Alex', 'envelope', 5)])