#include<stdio.h>

//Node Creation
struct Node
{
    int data;
    struct Node *next;
};

void insertBegin(struct Node** ref, int data)
{
    struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = data;  //Transfer data to Node
    temp->next = *ref;  //Making the next of new node as head
    *ref = temp;    //moving head to point the other node
}

void insertAny(struct Node* ref, int data)
{
    if(ref==NULL)
    {
        printf("The given previous node cannot be NULL.");
        return;
    }
    struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = data;
    temp->next = ref->next;
    ref->next = temp;
}

void append(struct Node **ref, int data)
{
    
}
int main()
{
    struct Node *root;
    root = (struct Node*)malloc(sizeof(struct Node));
}