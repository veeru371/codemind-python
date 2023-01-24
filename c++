#include<bits/stdc++.h>
using namespace std;
int main(){
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    vector<int>arr;
    arr.push_back(23);
    arr.push_back(646);
    arr.push_back(12);
    arr.push_back(56);
    arr.emplace_back(23222);
    for (auto it:arr){
        cout << it << " ";
    }
    cout <<"\n";
    cout <<"\n";
    vector<vector<int>>mat={{1,2,3},{4,5,6},{7,8,9}};
    for(int i=0;i<mat.size();i++){
        for( int j=0;j<mat.size();j++){
            cout << mat[i][j]<< " ";
        }
        cout<<"\n";
    }
    cout <<"\n";
    deque<int>de;
    de.push_front(1);
    de.push_front(2);
    de.push_back(5);
    de.push_front(6);
    for(auto it:de){
        cout << it<<" ";
    }
    vector<pair<int,int>>ve;
    ve.push_back({4,5});

    cout<<" ";
    set<int>se;
    se.insert(56);
    se.insert(75);
    se.insert(32);
    se.insert(12);
    se.insert(34);
    se.insert(67);
    auto it =se.find(75); // to check weather the element present in it or not
    auto it1 =se.find(9); // if it is not present it given last elem address
    cout <<*it<<" ";
    cout <<*it1;

    cout <<"\n";
    // stacks

    stack<int>st;
    st.push(10);
    st.push(20);
    st.push(30);
    st.push(40);
    cout << st.top();
    cout << "\n";
    cout << st.size()<<" \n";

    while(!st.empty()){
        cout<<st.top()<<" ";
        st.pop();
    }
    cout <<"\n";
    //queues

    queue<int>qe;
    qe.push(100);
    qe.push(200);
    qe.push(300);
    qe.push(400);
    cout <<qe.front()<<" \n";
    while(!de.empty()){
        cout <<qe.front()<<" ";
        qe.pop();
    }

    //priority_queue

    
    

}
