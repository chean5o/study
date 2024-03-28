#include <string>
#include <vector>

using namespace std;

void InsertSort(vector<int>& temp){
    for(int x = 1; x < temp.size(); x++){
        int y = temp[x];
        int tmp = x - 1;
        while(tmp >= 0 && temp[tmp] >= y){
            temp[tmp+1] = temp[tmp];
            tmp --;
        }
        temp[tmp+1] = y;
    }
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(int i = 0; i < commands.size(); i++){
        vector<int> temp;
        for (int j = commands[i][0] - 1; j < commands[i][1]; j++){
            temp.push_back(array[j]);
        }
        InsertSort(temp);
        answer.push_back(temp.at(commands[i][2] - 1));
    }
    return answer;
}