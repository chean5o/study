def solution(letter):
    answer = ''
    tmp = ''
    morse = { '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
              '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
              '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
              '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
              '-.--': 'y', '--..': 'z'}
    for i in letter:
        if i != ' ':
            tmp += i
        else:
            answer += morse.get(tmp, '') 
            tmp = ''
    answer += morse.get(tmp, '')
    return answer