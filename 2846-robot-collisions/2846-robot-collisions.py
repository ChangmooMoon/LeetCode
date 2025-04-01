from dataclasses import dataclass

@dataclass
class R:
    idx: int
    pos: int
    health: int
    dir: str

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robot_list = [R(idx, pos, health, dir) for idx, (pos, health, dir) in enumerate(zip(positions, healths, directions))]
        robot_list.sort(key=lambda x: x.pos)

        st = []
        for robot in robot_list: # dir: R, L
            if robot.dir == 'R':
                st.append(robot)
            else:
                while st and st[-1].dir == 'R' and robot.health > 0:
                    if st[-1].health == robot.health:
                        st.pop()
                        robot.health = 0
                    elif st[-1].health < robot.health:
                        st.pop()
                        robot.health -= 1
                    else: # st top health > robot.health
                        st[-1].health -= 1
                        robot.health = 0
                if robot.health > 0:
                    st.append(robot)
        st.sort(key=lambda x: x.idx)
        return [robot.health for robot in st]
