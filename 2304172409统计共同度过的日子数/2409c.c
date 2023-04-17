int countDaysTogether(char * arriveAlice, char * leaveAlice, char * arriveBob, char * leaveBob){
    int days[]={31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    char *arr,*lve;
    arr=strcmp(arriveAlice,arriveBob)>0? arriveAlice:arriveBob;
    lve=strcmp(leaveAlice,leaveBob)>0? leaveBob:leaveAlice;
    if (strcmp(arr,lve)>0) return 0;
    int res=0;
    for (int i=(arr[0]-'0')*10+arr[1]-'0';i<(lve[0]-'0')*10+lve[1]-'0';++i) res+=days[i-1];
    res=res+(lve[3]-'0')*10+lve[4]-'0'-((arr[3]-'0')*10+arr[4]-'0')+1;
    return res;
}