from tkinter import *
import pygame
import time
import random

root = Tk()
root.title("مسابقات كتاب مقدس")
root.geometry('550x550')

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound file
welcome_sound = pygame.mixer.Sound("welcome sound.mp3")
correct_sound = pygame.mixer.Sound("correct sound.mp3")
wrong_sound = pygame.mixer.Sound("wrong sound.mp3")
congrats_sound = pygame.mixer.Sound("congrats message.mp3")
tryagain_sound = pygame.mixer.Sound("tryagain message.mp3")

# global variable is_muted to keep track of the mute status.
is_muted = False

# create function to stop the welcome sound
def stopWelcomeSound():
    welcome_sound.stop()
# create function to play the welcome sound
def playWelcomeSound():
    welcome_sound.play()
# define run quiz game
def runQuizGame():
    # create a function to adjust the volume of all the sound objects accrodingly
    def toggleMute():
        global is_muted
        is_muted = not is_muted
        if is_muted:
            mute_button['text'] = "تم الكتم"
            stopWelcomeSound()  # Mute background music
            correct_sound.set_volume(0)  # Mute correct sound
            wrong_sound.set_volume(0)  # Mute wrong sound
            congrats_sound.set_volume(0)  # Mute congrats sound
            tryagain_sound.set_volume(0)  # Mute try again sound
        else:
            mute_button['text'] = "كتم"
            correct_sound.set_volume(1)  # Unmute correct sound
            wrong_sound.set_volume(1)  # Unmute wrong sound
            congrats_sound.set_volume(1)  # Unmute congrats sound
            tryagain_sound.set_volume(1)  # Unmute try again sound

    # Hide 2 frames (outside Function)
    first_frame.pack_forget()
    second_frame.pack_forget()
    # Create 3 frames
    top_frame = Frame(root, bg="#fff")
    middle_frame = Frame(root, bg="#fff")
    bottom_frame = Frame(root, bg="#fff")

    # Create Questions
    questions = ["ما معني اسم يسوع ؟",
                 "أين سكن إبرام بعد انفصال لوط عنه ؟",
                 "ما هو الطعام الذي كانت تنقله الغربان إلى إيليا ؟",
                 "بماذا قتل داود جليات الفلسطيني ؟",
                 "ما هي نتيجة الغضب من أخى باطلاً ؟ (مت 22:5)",
                 "ما هو الثمن الذى باع به يهوذا للرب يسوع ؟ (مت 15:26)",
                 "في أى سفر نجد الضربات العشر ؟",
                 "أين ورد الحديث عن بوعز ؟",
                 "من أول رجل تزوج امرأتين ؟ (تك 16)",
                 "ما معنى اسم نوح ؟",
                 "أين ولد الملك داود ؟ (1 صم 17)",
                 "كم سنة قضاها شمشون في القضاء ؟ (قض 31:16)",
                 "كم سنة عاشها نوح بعد الطوفان ؟ (تك 28:9)",
                 "من هى التى دهنت قدمي يسوع بطيب نادرين غالى الثمن ؟",
                 "متى كان أول سماح من الله للإنسان بأكل اللحوم ؟",
                 "من هو الذى كان طعامه جراداً وعسلاً برياً ؟",
                 "أين تقع مدينة صوعن ؟ (عدد 22:13)",
                 "أى من تلاميذ المسيح يقال له التوأم ؟ (يو 2:21)",
                 "من هو النبى الباكى ؟",
                 "من هو قائد المئة من الكتيبة التى تدعى الإيطالية ؟ (أع 10)",
                 "من اى سبط كان موسى ؟",
                 "أين كان يعيش رجل الله أيوب ؟",
                 "ما معنى اسم مريم ؟",
                 "ما معنى اسم اسرائيل ؟",
                 "كم يبلغ عدد أسفار العهد الجديد ؟",
                 "ما هو الإسم الآخر لسارة زوجة ابراهيم ؟",
                 "من هو الملك الذى أراد أن يقتل ابنه ولم يقتله ؟",
                 "ما الأصل اللغوى لكلمة انجيل ؟",
                 "ما معنى اسم أخنوخ ؟",
                 "كم عدد الأجيال من ابراهيم إلى ميلاد المسيح ؟"
                 ]

    # Create answers
    options = [
        ["يخلص", "الممسوع من الله", "يسمع", "الله معنا", "يخلص"],
        ["كنعان", "سدوم", "مصر", "العراق", "كنعان"],
        ["خبز فقط","فطير بعسل","المن","خبز ولحم","خبز فقط"],
        ["بالسيف","بالحجر","بالعصا","بالسيف","بالسهم"],
        ["مستوجب الحكم","مستوجب المجمع","مستوجب نار جهنم","مستوجب الحكم","كل ذلك"],
        ["30 من الفضة","50 من الفضة","40 من الفضة","30 من الفضة","20 من الفضة"],
        ["الخروج","التكوين","ارميا","الخروج","يشوع"],
        ["سفر راعوث","سفر أستير","سفر راعوث","سفر عوبديا","سفر نحميا"],
        ["ابراهيم","ابراهيم","يعقوب","لامك","اسحق"],
        ["حزن","راحة","فرح","حزن","دموع"],
        ["بيت لحم","بيت لحم","نينوى","أورشليم","يافا"],
        ["20","10","20","30","40"],
        ["سنة 350","سنة 350","سنة 250","سنة 150","سنة 50"],
        ["مريم أخت مرثا ولعازر","مريم زوجة كلوبا","مريم الخاطئة","مريم أخت مرثا ولعازر","طابيثا"],
        ["بعد الطوفان","بعد سقوط الإنسان","بعد الطوفان","بعد خراب سدوم وعمورة","بعد قتل هابيل"],
        ["يوحنا المعمدان","موسى","ايليا","يشوع","يوحنا المعمدان"],
        ["فى مصر على الضفة الشرقية من الدلتا","فى مملكة بابل","فى الاردن على ضفاف نهر الاردن","فى فلسطين بالقرب من أريحا","فى مصر على الضفة الشرقية من الدلتا"],
        ["توما","بطرس","توما","فيلبس","اندراوس"],
        ["ارميا","حزقيال","ارميا","اشعياء","دانيال"],
        ["كرنيليوس","كرنيليوس","بيلاطس","فيليمون","أنسيمس"],
        ["لاوى","يهوذا","لاوى","راؤيين","شمعون"],
        ["أرض عوص","أورشليم","أرض مصر","أرض عوص","أرض فلسطين"],
        ["العابدة أو المرتفعة","عذراء","طاهرة","العابدة أو المرتفعة","مرارة"],
        ["جندى الله","جندى الله","ابن الله","محبوب الله","مختار الله"],
        ["27","33","30","29","27"],
        ["ساراى","هاجر","راحيل","رفقة","ساراى"],
        ["شاول","داود","شاول","سليمان","حزقيا"],
        ["يونانى","آرامى","سريانى","عبرى","يونانى"],
        ["مكرس","أمين","مكرس","طاهر","جميل"],
        ["جيل 14","جيل 12","جيل 13","جيل 14","جيل 20"]
    ]
    # Randomize the order of questions and options
    combined = list(zip(questions, options))
    random.shuffle(combined)
    questions, options = zip(*combined)

    # In Top Frame
    # Create back button
    back_button = Button(top_frame, text="عودة", bg="orange", font=('Dubai Medium', 12),
                         command=lambda: [top_frame.pack_forget(), middle_frame.pack_forget(), bottom_frame.pack_forget(),
                                          first_frame.pack(fill="both"), second_frame.pack(fil="both", expand=True),note_label.pack_forget()])
    back_button.place(x=10,y=-6)

    # Create 2 keys binding as a shortcut for the back button
    root.bind("<Escape>",lambda event:[top_frame.pack_forget(), middle_frame.pack_forget(), bottom_frame.pack_forget(),
                                       first_frame.pack(fill="both"), second_frame.pack(fil="both", expand=True),note_label.pack_forget()])
    root.bind("<BackSpace>", lambda event:[top_frame.pack_forget(), middle_frame.pack_forget(), bottom_frame.pack_forget(),
                                           first_frame.pack(fill="both"), second_frame.pack(fil="both", expand=True),note_label.pack_forget()])
    # create mute sound button
    mute_button = Button(top_frame, text="كتم", bg="orange", font=('Dubai Medium', 12), command=toggleMute)
    mute_button.place(x=470, y=-5)

    # Create a key binding as a shortcut for the mute button
    root.bind("m", lambda event: toggleMute())
    score = 0
    score_label = Label(top_frame, text="النقاط: " + str(score), font=('Arial Bold', 20), bg="#fff")
    score_label.pack()
    # Create Label (Questions)
    question_label = Label(top_frame, height=5, width=39, bg='grey', fg="#fff", font=('Arial Bold', 20),
                           wraplength=1000)
    question_label.pack(pady=10)

    # Create Label for Countdown Timer
    countdown_label = Label(top_frame, text="الزمن: ", font=('Arial Bold', 20), bg="#fff")
    countdown_label.pack()

    # In Middle Frame
    # Create 4 options
    v = StringVar(middle_frame)
    v.set("None")
    option1 = Radiobutton(middle_frame, bg="#fff", variable=v, font=('Arial', 20))
    option2 = Radiobutton(middle_frame, bg="#fff", variable=v, font=('Arial', 20))
    option3 = Radiobutton(middle_frame, bg="#fff", variable=v, font=('Arial', 20))
    option4 = Radiobutton(middle_frame, bg="#fff", variable=v, font=('Arial', 20))
    option1.grid(sticky='W', row=1, column=0)
    option2.grid(sticky='W', row=2, column=0)
    option3.grid(sticky='W', row=3, column=0)
    option4.grid(sticky='W', row=4, column=0)

    # In Bottom Frame
    # create Next Button
    button_next = Button(bottom_frame, text="التالي", bg="Orange", font=('Calibri', 20),
                         command=lambda: [displayNextQuestion(),countdownTimer()])
    # create 2 keys binding as a shortcut for next button
    root.bind("<space>",lambda event: [displayNextQuestion(),countdownTimer()])
    root.bind("<Return>",lambda event: [displayNextQuestion(),countdownTimer()])
    # Variables to track the quiz progress
    index = 0
    correct = 0
    # create a function to disable radiobuttons
    def disableButtons(state):
        option1['state'] = state
        option2['state'] = state
        option3['state'] = state
        option4['state'] = state
    # Define countdown timer function
    def countdownTimer():
        global score
        score = 0 # initial score
        remaining_time = 20  # Set the initial time (in seconds)
        while remaining_time > 0:
            if not v.get() == "None":
                countdown_label['text'] = "! هيا، تابع الأسئلة"
                break  # Exit the loop if an option is selected
            countdown_label['text'] = "الزمن: " + str(remaining_time)
            root.update()  # Update the Tkinter window to reflect the changes
            time.sleep(1)  # Wait for 1 second
            remaining_time -= 1
            countdown_label['text'] = " !انتهى الوقت " # countdown timer finished
        disableButtons('disabled')
        if v.get() == "None":
            button_next['command'] = checkAnswer()



    def checkAnswer():
        nonlocal correct, index, score
        # The selected option is 1st index
        selected_option = v.get()
        if selected_option == options[index][0]:  # If correct option, display green label
            button_next.pack(pady=10)
            question_label['bg'] = 'green'
            question_label['text'] = "صحيح"
            question_label['font'] = ('Calibri', 22)
            correct += 1
            score = correct * 2  # Reset the score and increment it by 2 for each correct answer
            score_label['text'] = "النقاط: " + str(score)
            correct_sound.play()  # Play correct sound
        else:  # If wrong option, display red label
            button_next.pack(pady=10)
            question_label['bg'] = 'red'
            question_label['text'] = "خطأ"
            question_label['font'] = ('Calibri', 22)
            wrong_sound.play()  # Play wrong sound
        disableButtons('disable')  # Disable buttons
        index += 1



    def displayNextQuestion():
        nonlocal index, correct, score
        if button_next['text'] == 'إعادة المحاولة':  # if restart clicked, play again
            countdown_label.pack()
            correct = 0
            index = 0
            question_label['bg'] = 'grey'
            button_next['text'] = 'التالي'
            score_label.pack()  # display the score
        if index == len(options):
            button_next['text'] = 'إعادة المحاولة'
            if correct >= len(options) / 2 :  # if correct, green bg label
                question_label['text'] = "!! تهانينا أحسنت" + "\n" + "لقد حصلت على " + str(score) + " نقطة"
                question_label['bg'] = 'green'
                question_label['font'] = ('Calibri', 24)
                congrats_sound.play()  # play congrats sound
                score = 0
                score_label['text'] = "النقاط: " + str(score)
                countdown_label.pack_forget()  # Hide countdown timer label
            else: # if wrong, red bg label
                question_label['text'] = '!! اعد المحاولة مرة أخرى'
                question_label['bg'] = 'red'
                question_label['font'] = ('Calibri', 24)
                tryagain_sound.play()  # play try again sound
                countdown_label.pack_forget()  # Hide countdown timer label
        else:
            button_next.pack_forget() # hide the button
            question_label['text'] = questions[index] # Display the Questions
            # Set the options and their values correctly
            option1['text'] = options[index][1]
            option1['value'] = options[index][1]
            option2['text'] = options[index][2]
            option2['value'] = options[index][2]
            option3['text'] = options[index][3]
            option3['value'] = options[index][3]
            option4['text'] = options[index][4]
            option4['value'] = options[index][4]
            disableButtons('normal')  # Enable buttons after restarting
            v.set("None")  # to choose again any option
            question_label['bg'] = 'grey'
            question_label['font'] = ('Arial Bold', 20)

        if index == len(options) - 1:  # if check result clicked, click restart
            button_next['text'] = 'التحقق من النتائج'

    # Connect the checkAnswer() function to the radio buttons' selection
    option1.config(command=checkAnswer)
    option2.config(command=checkAnswer)
    option3.config(command=checkAnswer)
    option4.config(command=checkAnswer)

    # Pack 3 frames
    top_frame.pack(fill="both")
    middle_frame.pack(fill="both", expand="true")
    bottom_frame.pack(fill="both")

    # Call the function to display the next question
    displayNextQuestion()
    countdownTimer()  # Start the countdown timer

############END Function############

# create 2 frames
first_frame = Frame(root, bg='#fff')
second_frame = Frame(root, bg="#fff")
# play welcome sound after 5 seconds
root.after(5000, welcome_sound.play)
# create BIG welcome label text
welcome_label = Label(first_frame, bg="#fff", font=("Urdu Typesetting", 60), text="مسابقات الكتاب المقدس")
welcome_label.pack()
# Create 2 buttons to call the function & 1 button to exit
start_button = Button(second_frame, text="ابدأ المسابقة", font=('Dubai Medium', 20), bg="GreenYellow",
                      command=lambda: [stopWelcomeSound(), runQuizGame()])
start_button.pack()

Restart_button = Button(second_frame, text="إعادة المسابقة", font=('Dubai Medium', 20), bg="orange",
                        command=lambda: [stopWelcomeSound(), runQuizGame()])
Restart_button.pack(pady=10)
# create 2 keys binding as shortcut for starting quiz game
root.bind("<Return>",lambda event: [stopWelcomeSound(), runQuizGame()])
root.bind("<space>",lambda event: [stopWelcomeSound(), runQuizGame()])
quit_button = Button(second_frame, text="خروج", font=('Dubai Medium', 20), bg="orange red",
                     command=root.destroy)
quit_button.pack()
# create key binding as shortcut for exit quiz game
root.bind("<Escape>",lambda event: root.destroy())
# create note label
note_label = Label(second_frame, font=("Arial Bold", 22), bg='#fff', text="(أمامك رسالة صوتية يمكنك التخطي)")
# display note label after 5 seconds
root.after(5000, note_label.pack)
# Hide the note label after 29 & half seconds
note_label.after(29500, note_label.pack_forget)
# create Designer label
designer = Label(second_frame, font=("Tahoma", 20), bg='#fff', text="إعداد/ مينا روبير مجدى")
designer.pack(pady=10)
# pack 2 frames
first_frame.pack(fill="both")
second_frame.pack(fil="both", expand=True)
root.mainloop()  # GUI - End
