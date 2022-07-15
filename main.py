# get user name
u_name = input('What\'s your name?: ')

# get user hourly wage
h_wage = int(input('What\'s your hourly wage?: $'))

#daily wage function
def daily_wage():
  d_wage = 8 * h_wage
  print(f'Your daily salary is ${d_wage}')

#weekly wage function
def weekly_wage():
  w_wage = 40 * h_wage
  print(f'Your weekly salary is ${w_wage}')

#monthly wage function
def monthly_wage():
  m_wage = 160 * h_wage
  print(f'Your monthly salary is ${m_wage}')

#yearly wage function
def yearly_wage():
  y_wage = 2040 * h_wage
  print(f'Your yearly salary is ${y_wage}')

daily_wage()
weekly_wage()
monthly_wage()
yearly_wage()