from flask import Flask, render_template

import utils
from utils import load_candidates_from_json, get_candidates_by_name, get_candidate, get_candidates_by_skill

def main():
     DATA_SOURCE_ = "candidates.json"
     candidates_list = load_candidates_from_json(DATA_SOURCE_)

     # создание экземпляра класса Flask
     app = Flask(__name__)

     # создание декораторов и функций, передача данных в шаблоны
     @app.route("/")
     def page_index():
         return render_template('list.html', candidates_list=candidates_list)

     @app.route("/candidate/<int:id>/")
     def page_candidates(id):
         candidate = utils.get_candidate(candidates_list, id)
         if candidate:
             return render_template('card.html', candidate=candidate)
         else:
             return "Candidate not found"

     @app.route("/search/<candidate_name>/")
     def page_search_candidates(candidate_name):
         list_search = get_candidates_by_name(candidates_list, candidate_name)
         count_candidates = len(list_search)
         if list_search:
             return render_template('search.html', list_search=list_search, count_candidates=count_candidates)
         else:
             return "Candidate not found"

     @app.route("/skill/<skill_name>")
     def page_skill_candidates(skill_name):
         list_candidates = get_candidates_by_skill(candidates_list, skill_name)
         count_candidates = len(list_candidates)
         if list_candidates:
            return render_template('skill.html', list_candidates=list_candidates, count_candidates=count_candidates)
         else:
             return "Candidate not found"

     # запуск сервера
     app.run()




if __name__ == '__main__':
    main()


