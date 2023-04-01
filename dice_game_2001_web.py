from flask import Flask, request, render_template
import random

size_list = [3, 4, 6, 8, 10, 12, 20, 100]  # valid dice sizes


app = Flask(__name__)



def calculate_score(score, roll):
    if sum(roll) == 7:
        score = score // 7
    elif sum(roll) == 11:
        score = score * 11
    else:
        score += sum(roll)

    return score


@app.route("/", methods=['POST', 'GET'])
def roll(num=2):

    if request.method == "GET":
        return render_template("form.html")
    else:
        player_size = int(request.form.get("dice"))
        player_score = 0
        player_score = int(request.form.get("players_score", 0))
        comp_score = 0
        comp_score = int(request.form.get("comp_score", 0))

        while True:
            player_size = int(request.form.get("dice"))
            comp_size = size_list[random.randint(0, 7)]

            player_roll = [random.randint(0, player_size) for i in range(num)]
            comp_roll = [random.randint(0, comp_size) for i in range(num)]

            player_score = calculate_score(player_score, player_roll)
            comp_score = calculate_score(comp_score, comp_roll)

            # player_roll_str = ", ".join([str(i) for i in player_roll])
            # comp_roll_str = ", ".join([str(i) for i in comp_roll])
            if player_score < 2001 and comp_score < 2001:
                return render_template("form.html", player_score=player_score, comp_score=comp_score)
            elif player_score > 2001 and comp_score <= 2001:
                result = "Player wins!"
                return render_template("form.html", player_score=player_score, comp_score=comp_score, result=result)
            elif player_score <= 2001 and comp_score > 2001:
                result = "Computer wins!"
                return render_template("form.html", player_score=player_score, comp_score=comp_score, result=result)

# z innego zadania
# def guess():
#     if request.method == "GET":
#         return render_template("form.html")
#     else:
#         min = int(request.form.get("min"))
#         max = int(request.form.get("max"))
#         answer = request.form.get("answer")
#         # guess = (max - min) // 2 + min
#         guess = int(request.form.get("guess", 500))
#
#         if answer == "Too big":
#             max = guess
#         elif answer == "Too small":
#             min = guess
#         elif answer == "You win!":
#             return render_template("form.html", guess=guess)
#
#         guess = (max - min) // 2 + min
#
#         return render_template("form.html", guess=guess, min=min, max=max)




if __name__ == "__main__":
    app.run(debug=True, port=5002)