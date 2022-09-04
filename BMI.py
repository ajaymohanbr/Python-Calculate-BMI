height = float(input('Inform your height in meters: '))
weight = float(input('Inform your weight in kg: '))
IMC = weight/height**2  #IMC = Body Mass Index


if IMC < 18.5 :
    print(f'BMI= {IMC:.2f}')
    print('Underweight')  
    
elif IMC >=18.5 and IMC <= 24.9:
    print(f'BMI= {IMC:.2f}')
    print('Healthy')


elif IMC >=24.9 and IMC <= 30:
    print(f'BMI= {IMC:.2f}')
    print('Overweight')  
    
if IMC > 30 :
    print(f'BMI= {IMC:.2f}')
    print('Obese')        