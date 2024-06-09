from typing import List, Tuple
def distance(pt1, pt2)->float:
    return ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**0.5

def brute_force(points):
    n=len(points)
    min_dis=float('inf')
    for i in range(n):
        for j in range(i+1, n):
            min_dis=min(min_dis, distance(points[i], points[j]))
    return min_dis

def conquer(points_chosen:List[Tuple[int, int]], min_dis:float)->float:
    n=len(points_chosen)
    # min_dis=float('inf')
    points_chosen.sort(key=lambda point: point[1])
    for i in range(n):
        j=i+1
        while j<n and points_chosen[j][1]-points_chosen[i][1]<min_dis:
            min_dis=min(min_dis, distance(points_chosen[i], points_chosen[j]))
            j+=1
    return min_dis

def divide(sorted_x:List[Tuple[int, int]])->float:
    n=len(sorted_x)
    if n<=3:
        return brute_force(sorted_x)
    mid=n//2
    # d=float('inf')
    # left conquer
    dl=divide(sorted_x=sorted_x[:mid])
    # right conquer
    dr=divide(sorted_x=sorted_x[mid:])
    d=min(dl, dr)
    mid_point_x=sorted_x[mid][0]
    point_chosen=[point for point in sorted_x if abs(point[0]-mid_point_x)<d]
    return min(d, conquer(point_chosen, d))

def main():
    points=[(2, 3), (10, 4), (5, 6), (7, 10), (4, -1)]#sqrt(20)
    points_sorted_x = sorted(points, key=lambda point: point[0])
    min_distance=divide(sorted_x=points_sorted_x)
    print(f"the min distance among points is {min_distance}")

if __name__=='__main__':
    main()
