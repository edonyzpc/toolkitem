#include <iostream>
typedef Stack DList;
#define stack_init list_init;
#define stack_destroy list_destroy;
using namespace std;

int main() {
    int tmp;
    // tmp_double counter for timer
    double tmp_double;
    std::cout<<"test"<<std::endl;
    for(int i=0;i<10;++i) {
        std::cout<<i+10<<std::endl;
    }
    for(int i=0;i<10;++i) {
        std::cout<<i+1<<std::endl;
    }
}

void swap(void *key1, void key2);
