import inquirer

locationQuestions = [
  inquirer.Text('city', message="Which city's weather are you interested in?"),
  inquirer.Text('state', message="In which state is this city located?"),
]