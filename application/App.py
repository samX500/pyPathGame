from environment.Arena_factory import Arena_factory


class App():

    if __name__ == '__main__':
        arena = Arena_factory.build_random_arena(10, 10)
        print(arena)