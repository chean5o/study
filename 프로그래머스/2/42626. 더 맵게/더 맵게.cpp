#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq;
    for(auto s:scoville){
        pq.push(s);
    }    
    while(!pq.empty()){
        auto cur = pq.top();
        if(cur<K){
            answer++;
            pq.pop();
            if(!pq.empty()){
                int new_food = cur+(2*pq.top());
                pq.pop();
                pq.push(new_food);                
            }else{
                return -1;   
            }
        }else{
            break;
        }
    }    
    return answer;    
}