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
    for startWord in reference:
        currentMaxScore = 0
        w1 = wordnet.synsets(startWord)[0]
        for checkedWord in words:
            w2 = wordnet.synsets(checkedWord)[0]
            currentScore = w1.wup_similarity(w2)
            if currentScore > currentMaxScore:
                currentMaxScore = currentScore
        totalScore += currentMaxScore * 10
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


reference = "A dog on a hill"
guesses = ["A fox beneath the mountain", "A dog on the ocean", "pickle"]

print(postProcessing(reference, guesses))