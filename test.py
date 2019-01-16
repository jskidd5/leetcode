class Solution:

    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        speed_stack = []
        map_car = []
        car_cnt = len(position)
        if car_cnt == 0:
            return 0
        for i in range(car_cnt):
            map_car.append([position[i], speed[i]])
        map_car.sort(reverse=True)
        speed_stack.append([map_car[0][1], (target - map_car[0][0]) / map_car[0][1]])
        for i in range(1, car_cnt):
            if map_car[i][1] > speed_stack[-1][0] and speed_stack[-1][1] * map_car[i][1] + map_car[i][0] >= target:
                pass
            else:
                speed_stack.append([map_car[i][1], (target - map_car[i][0]) / map_car[i][1]])
        return len(speed_stack)


s = Solution()
print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
