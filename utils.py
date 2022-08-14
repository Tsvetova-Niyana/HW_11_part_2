import json

from classes import Candidate


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    candidates_list = []
    with open(path, encoding='utf-8') as file_json:
        file_list = json.load(file_json)
        for candidate in file_list:
            candidates = Candidate(candidate['id'], candidate['name'], candidate['picture'], candidate['position'], candidate['skills'])
            candidates_list.append(candidates)
    return candidates_list

def get_candidate(candidates_list, candidate_id):
    """возвращает одного кандидата по его id"""
    for candidate in candidates_list:
        if int(candidate.id) == int(candidate_id):
            return candidate


def get_candidates_by_name(candidates_list, candidate_name):
    """возвращает кандидатов по имени"""
    list_search = []
    for candidate in candidates_list:
        if candidate_name in candidate.name:
            list_search.append({'id': candidate.id, 'name': candidate.name})
    return list_search


def get_candidates_by_skill(candidates_list, skill_name):
    """возвращает кандидатов по навыку"""
    list_candidates = []
    for candidate in candidates_list:
        if skill_name.lower() in candidate.skills.lower():
            list_candidates.append({'id': candidate.id, 'name': candidate.name})
    return list_candidates