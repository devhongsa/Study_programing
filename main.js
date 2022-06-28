function solution(N, arr) {
    let res = 0;

    for (i=0; i<arr.length-1; i++){
        for (j=i+1; j<arr.length; j++){
            if (arr[i] + arr[j] == 0) return 2
        }
    }

    for (i=0; i<arr.length-2; i++){
        for (j=i+1; j<arr.length-1; j++){
            for (m=j+1; m<arr.length; m++){
                if (arr[i] + arr[j] + arr[m] == 0) return 3
            }
        }
    }

    for (i=0; i<arr.length-3; i++){
        for (j=i+1; j<arr.length-2; j++){
            for (m=j+1; m<arr.length-1; m++){
                for (n=m+1; n<arr.length; n++){
                    if (arr[i] + arr[j] + arr[m] + arr[n] == 0) return 4
                }
            }
        }
    }

    for (i=0; i<arr.length-4; i++){
        for (j=i+1; j<arr.length-3; j++){
            for (m=j+1; m<arr.length-2; m++){
                for (n=m+1; n<arr.length-1; n++){
                    for (b=n+1; b<arr.length; b++){
                        if (arr[i] + arr[j] + arr[m] + arr[n] + arr[b] == 0) return 5
                    }
                }
            }
        }
    }

    return -1;
}