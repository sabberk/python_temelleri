class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        # Küçük/büyük harf farketmez karşılaştırma
        return self.answer.lower() == answer.lower()


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0  # 0'dan başlıyoruz

    def getQuestion(self):
        if self.questionIndex < len(self.questions):
            return self.questions[self.questionIndex]
        return None

    def displayQuestion(self):
        question = self.getQuestion()
        if question is None:
            self.showScore()
            return

        print(f"\nSoru {self.questionIndex + 1}: {question.text}")
        for idx, choice in enumerate(question.choices, start=1):
            print(f"  {idx}. {choice}")

        # Kullanıcıdan geçerli bir seçenek numarası alana kadar tekrar et
        while True:
            answer = input("Cevabınız (seçenek numarası): ").strip()
            if answer.isdigit():
                num = int(answer)
                if 1 <= num <= len(question.choices):
                    selected_choice = question.choices[num - 1]
                    break
            print("Geçersiz giriş. Lütfen seçenek numarasını girin.")

        self.guess(selected_choice)

    def guess(self, answer):
        question = self.getQuestion()
        if question is None:
            return

        if question.checkAnswer(answer):
            print("Doğru!\n")
            self.score += 1
        else:
            print(f"Yanlış! Doğru cevap: {question.answer}\n")

        self.questionIndex += 1
        self.loadQuestion()

    def loadQuestion(self):
        if self.questionIndex >= len(self.questions):
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Quiz bitti. Skorunuz: {self.score} / {len(self.questions)}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f"\nQuestion {questionNumber} of {totalQuestion}".center(60, "*"))


