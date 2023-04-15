/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* gardenNoAdj(int n, int** paths, int pathsSize, int* pathsColSize, int* returnSize){
    int neighbor[n][3];
    memset(neighbor,0,sizeof(int)*3*n);
    //build the neighbor dict
    for(int i=0;i<pathsSize;++i){
        int* path=paths[i];
        int largeri=path[0]>path[1] ? 0:1;
        for (int j=0;j<3;++j){
            if (neighbor[path[largeri]-1][j]==0){
                neighbor[path[largeri]-1][j]=path[1-largeri];
                break;
            }
        }
    }
    //dye it babe!
    int *res = (int *)malloc(sizeof(int)*n);
    memset(res,0,sizeof(int)*n);
    for (int i=0;i<n;++i){
        for (int color=1;color<5;++color){
            //WOW, only choice...
            if(color==4){
                res[i]=color;
                break;
            }
            //try try try
            for (int j=0;j<3;++j){
                if (neighbor[i][j]==0){
                    res[i]=color;
                    break;
                }
                else if(res[neighbor[i][j]-1]==color) break;
            }
            if (res[i]!=0) break;
        }
    }
    *returnSize = n;
    return res;
}
