import flet as ft
import time

def main(page: ft.Page):
    page.title = 'Training Program'
    page.bgcolor = '#43464B'
    page.vertical_alignment = ft.alignment.center
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width =460
    page.window.height = 600

    

    progress = ft.ProgressBar(width=100,value = 0,visible= False)

    start_text = ft.Text('This program will help you increase your one-rep max in 12 weeks')

    programm_text = ft.Text('')

    def round_to_five(weight):
        return round(weight / 5) * 5

    def round_to_nearest_2_5(x):
        return round(x / 2.5) * 2.5

    def format_weight(w):
        if w.is_integer():
            return int(w)
        return w
    
    def program(_):
        
        progress.visible = True

        programma = {
            '1week': [70, 5, 5],
            '2week': [72.5, 5, 5],
            '3week': [75, 4, 5],
            '4week': [85, 3, 3],
            '5week': [88, 4, 2],
            '6week': [70, 3, 5],
            '7week': [77.5, 5, 4],
            '8week': [87.5, 3, 2],
            '9week': [90, 3, 2],
            '10week': [70, 3, 3],
            '11week': [85, 2, 2],
            '12week': [105, 1, 1]
        }

        max_lift = float(current_max.value)

        total = len(programma)

        new_programma = {}
        for i,(week, values) in enumerate(programma.items()):
            percent = values[0] / 100
            sets = values[1]
            reps = values[2]
            weight = max_lift * percent
            rounded_weight = round_to_nearest_2_5(weight)
            rounded_weight = format_weight(rounded_weight)
            new_programma[week] = [rounded_weight, sets, reps]
            progress.value = (i + 1) / total
            time.sleep(0.3)
            page.update()
        
        programm_text.value = f'1st week: {new_programma['1week'][0]}kg, podhodov {new_programma['1week'][1]}, povtorov{new_programma["1week"][2]}'
            
        current_max.value = ''
        progress.value = 1
        if progress.value == 1:
            progress.visible = False
            gen_button.disabled = True
            navigation2.visible = True
        page.update()
        
    # def clear(_):
    #     if programm_text3.value != '':
    #         error_text.value = ''
    #         programm_text.value = ''
    #         programm_text1.value = ''
    #         programm_text2.value = ''
    #         programm_text3.value = ''
    #         progress.value = 0
    #     else:
    #         error_text.value = 'Generate first or wait until its finished'
    #         error_text.color = ft.Colors.RED
    #     page.update()
    
    
    # def TXT(_):
    #     with open('Training.txt','w') as file:
    #         if programm_text3.value != '':
    #             file.write("Training plan for 12 weeks:\n")
    #             file.write(programm_text1.value + "\n")
    #             file.write(programm_text2.value + "\n")
    #             file.write(programm_text3.value + "\n")
    #             error_text.value = 'File saved as Training.txt'
    #             error_text.color = ft.Colors.WHITE
    #         else:
    #             error_text.value = 'Generate first to save it'
    #             error_text.color = ft.Colors.RED
    #         page.update()
    
    def test(_):
        value = current_max.value
        try:
            float(value)
            gen_button.disabled = False
        except:
            gen_button.disabled = True
        page.update()



    gen_button = ft.ElevatedButton('Generate',on_click = program, disabled= True)
 
    # button2 = ft.ElevatedButton('Clear',on_click= clear)

    # button3 = ft.ElevatedButton('Convert to TXT',on_click = TXT)

    current_max = ft.TextField(label = 'Input your current one-rep max',on_submit= program, on_change= test)


    page_one = ft.Column(
        [
            start_text,
            current_max,
            gen_button,
            progress
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page_two = ft.Column(
        [
            programm_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page1 = ft.Container(
        page_one,
        alignment=ft.alignment.center,
        expand=True
    )

    page2 = ft.Container(
        page_two,
        alignment=ft.alignment.center,
        expand=True
    )

    def navigate(_):
        index = page.navigation_bar.selected_index
        page.clean()
        if index == 0:
            page.add(page1)
        elif index == 1:
            page.add(page2)
    
    navigation1 = ft.NavigationBarDestination(icon=ft.Icons.ABC ,label = '1st page')
    navigation2 = ft.NavigationBarDestination(icon=ft.Icons.ABC, label = '2nd page',visible= False)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            navigation1,navigation2
        ],on_change= navigate
    )

    page.add(page1)




ft.app(target = main)