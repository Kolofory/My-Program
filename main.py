from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

class MainUI(App):
    def build(self):
        main_bl = BoxLayout(orientation='vertical')
        bl = BoxLayout()
        
        self.text_input = TextInput(multiline=False, hint_text='Напишіть квадратне рівняння', font_size=30, size_hint=(1, .3))
        
        btn = Button(text='x²', on_press=self.add_text_input, font_size=20, size_hint=(1, .2))

        d_button = Button(text='Дестримінант рівняння', on_press=self.button_press, font_size=20)
        k_button = Button(text='Корінні рівняння', on_press=self.button_press, font_size=20)

        main_bl.add_widget(self.text_input)
        bl.add_widget(d_button)
        bl.add_widget(k_button)

        main_bl.add_widget(bl)
        main_bl.add_widget(btn)
        
        return main_bl
    
    def search_numbers(self, equation):
        self.signs = ['+', '=', 'x', '²']
        self.num = {}
        for i in self.signs:
            equation = equation.replace(i, ' ')
        numbers = equation.split()
        self.num['a'] = numbers[0]
        self.num['b'] = numbers[1]
        self.num['c'] = numbers[2]

        return self.num

    def search_discriminant(self, a, b, c):
        self.discriminant = b**2 - 4*a*c
        return self.discriminant

    def search_x1_x2(self, b, c):
        if b < 0:
            x1 = b
            x2 = b
            b = -b
        else:
            x1 = -b
            x2 = -b
        if self.discriminant > 0:
            for i in range(b*2):
                x1 += 1
                x2 = -b
                for j in range(b*3):
                    if x1 + x2 == b and x1 * x2 == c:
                        return x1, x2
                        break
                    else:
                        x2 += 1
    
    def button_press(self, instance):
        try:
            self.equation = self.text_input.text
            num = self.search_numbers(self.equation)
            self.discriminant = self.search_discriminant(int(num['a']), int(num['b']), int(num['c']))
            if instance.text == 'Дестримінант рівняння':
                self.text_input.text = f'Дестримінант рівняння: {self.discriminant}'
            elif instance.text == 'Корінні рівняння':
                x1, x2 = self.search_x1_x2(int(num['b']), int(num['c']))
                self.text_input.text = f'x1 = {x1}\nx2 = {x2}\nДескримінант: {self.discriminant}'
        except:
            self.text_input.text = ''

    def add_text_input(self, instance):
        self.text_input.text = self.text_input.text + instance.text

if __name__ == '__main__':
    MainUI().run()