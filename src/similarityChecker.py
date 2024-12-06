from nltk.corpus import wordnet

def preProcessing(sentence):
    removableWords = ['the', 'a', 'is', 'on', 'there', 'very', 'really', 'much']
    sentence = sentence.lower()
    words = sentence.split(' ')
    for word in removableWords:
        if word in words:
            words.remove(word)

    return words

def processing(reference, words):
    totalScore = 0
    specialWords = []
    for startWord in reference:
        currentMaxScore = 0
        if len(wordnet.synsets(startWord)) == 0:
            specialWords.append(startWord)
            continue
        w1 = wordnet.synsets(startWord)[0]
        for checkedWord in words:
            if len(wordnet.synsets(checkedWord)) == 0:
                continue
            w2 = wordnet.synsets(checkedWord)[0]
            currentScore = w1.wup_similarity(w2)
            if currentScore > currentMaxScore:
                currentMaxScore = currentScore
        totalScore += currentMaxScore * 10

    for specialWord in specialWords:
        if specialWord in words:
            totalScore += 5
    return totalScore

def postProcessing(reference, answers):
    scores  = []
    referenceWords = preProcessing(reference)
    print(referenceWords)
    for answer in answers:
        answerP = preProcessing(answer)
        score = processing(referenceWords, answerP)
        scores.append(score)
    winner = scores.index(max(scores))
    return winner