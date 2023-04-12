#include <string>
#include <vector>
#include <array>

using namespace std;
#define NUM_ALPHA (26)

// 각 스킬 트리마다 유효성을 검사하는 함수
// @param skillTree: 검사 할 스킬 트리
// @param prior: 스킬의 우선 순위 배열
bool CheckValid(const std::string& skillTree, const std::array<int, NUM_ALPHA>& prior) {
    std::array<bool, NUM_ALPHA> learned; // 학습 여부 테이블
    learned.fill(false); // false로 초기화 (초기 상태: 아무것도 배우지 않은 상태)

    // 스킬 트리의 각 스킬을 평가
    for (int i = 0; i < skillTree.size(); ++i) {
        const int curSkillIndex = skillTree[i] - 'A'; // 현재 스킬
        const int priorSkillIndex = prior[curSkillIndex]; // 선행 스킬

        // 선행 스킬이 없거나, 선행 스킬이 이미 배운 스킬이라면 현재 스킬 학습
        if (priorSkillIndex == -1 || learned[priorSkillIndex] == true) {
            learned[curSkillIndex] = true;
        }
        // 그렇지 않다면 유효성 검사 실패
        else {
            return false;
        }
    }

    // 스킬 트리의 모든 스킬을 배울 수 있다면 유효성 검사 성공
    return true;
}

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;

    // 선행 스킬 테이블
    std::array<int, NUM_ALPHA> prior;
    prior.fill(-1); // -1 : 선행 스킬이 없음을 의미.

    for (int i = 0; i < skill.size() - 1; ++i) {
        const int curIndex = skill[i] - 'A';
        const int nextIndex = skill[i + 1] - 'A';
        // cur이 next보다 선행함
        prior[nextIndex] = curIndex;
    }

    // 스킬 트리마다 유효성 검사.
    for (const std::string& skillTree : skill_trees) {
        const bool result = CheckValid(skillTree, prior);

        // 유효성 검사 통과 시 answer 1 만큼 증가.
        if (result == true) {
            ++answer;
        }
    }

    return answer;
}