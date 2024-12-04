movies = ['어벤져스','레슬러','챔피언','얼리맨','당갈','콰이어트 플레이스']
#예매순위 4위만 출력
print("4위 : {}".format(movies[3]))
#예매순위 1~2위까지 리스트로 출력
movieA = movies[:2]
print("1~2위 : {}" .format(movieA))

#예매순위 4~5위까지 출력
movieB= movies[3:5]
print("4~5위 : {}" .format(movieB))

#1~2, 4~5위를 추출한 리스트를 결합하여 새로운 리스트를 생성하세요
net_Movies = movieA + movieB
print(net_Movies) 