# get user name
u_name = input('What\'s your name?: ')

# get user hourly wage
h_wage = int(input('What\'s your hourly wage?: $'))

#daily wage function
def daily_wage():
  d_wage = 8 * h_wage
  print(f'Your daily salary is ${d_wage}')

daily_wage()