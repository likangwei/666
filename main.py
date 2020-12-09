# coding=utf-8
import os


def life():
    """
    只要没死，就会一天天的过
    :return:
    """
    while not die:
        yield new_day


def better_plan(oneday):
    """
    反思
    :param oneday:
    :return: plan
    """
    # 好的继续保持
    # 不好的改正
    os.system('open https://github.com/likangwei/666/issues')


def plan_every_day():
    """
    PDCA
    https://baike.baidu.com/item/PDCA%E5%BE%AA%E7%8E%AF/5091521
    1、计划阶段。要通过市场调查、用户访问等，摸清用户对产品质量的要求，确定质量政策、质量目标和质量计划等。包括现状调查、分析、确定要因、制定计划。
    2、设计和执行阶段。实施上一阶段所规定的内容。根据质量标准进行产品设计、试制、试验及计划执行前的人员培训。
    3、检查阶段。主要是在计划执行过程之中或执行之后，检查执行情况，看是否符合计划的预期结果效果。
    4、处理阶段。主要是根据检查结果，采取相应的措施。巩固成绩，把成功的经验尽可能纳入标准，进行标准化，遗留问题则转入下一个PDCA循环去解决。
    :return:
    """


def get_okr_for_oneday():
    """
    制定一天的okr
    """


def get_yesterday_result():
    """
    从大脑里回忆
    """


def fix_bug():
    """
    每天都要做的，就是修复bug
    因为系统是自动化运行的
    """
    # 打开 https://github.com/likangwei/666
    # 过滤出 open的bug
    # 修复代码
    pass


def change_direction():
    """
    方向错误，调整方向
    """
    # 1. 建立一个新的issue
    # 2. label为 enhancement
    "https://github.com/likangwei/666"


def 一天的流程():
    """
    思考昨天哪里做的不好，并进行改进
    """
    # 修复系统bug
    bugs = get_bugs()  # https://github.com/likangwei/666/issues
    for bug in bugs:
        if need_fix(bug):  # 高频的问题，才有解决的必要
            fix_bug(bug)

    the_one = "帮大家越来越好"
    # 分拆目标, 包含 新建、进行中
    direction = get_direction(the_one)
    # 探索方向
    result = discovery(direction)

    # 正确的方向，加大投入
    if direction_right(direction, result):
        # 加大投入
        more_gold(direction)
    else:
        # 错误的方向，及时调整
        new_direction = change_direction()

    yesterday_result = get_yesterday_result()
    try:
        写公众号进行反思(yesterday_result)
    except 日更中断:
        # - reopen 问题日志
        # - 修复bug
        "https://github.com/likangwei/666/issues/11"
    except:
        # 1. 建立一个新的issue
        # 2. label为bug
        # 3. 如果the issue already exist，标记为 duplicate
        "https://github.com/likangwei/666"


def 帮大家越来越好():
    """
    如何帮大家越来越好
    """
    for new_day in life():
        一天的流程(new_day)


def can_do(task):
    if maybe_die(task):
        return False
    return True


def problem_filter(problem):
    """
    一件事的 能做的 估值
    """
    # 如果有生命风险，坚决不做
    if if_will_die(problem):
        return -1

    # 如果不能帮自己成长，那就是垃圾
    if if_cant_grow(problem):
        return 0

    # 返回能有多么帮自己成长
    return 有多么适合磨炼底层能力


def 让自己越来越硬(problem):
    """
    https://github.com/likangwei/666/issues/1
    不断发现问题，然后决定要不要解决
    :param problem:
    :return:
    """
    # 排序出来最有挑战的
    can_grow_choices.sort()
    return can_grow_choices.pop(0)


if __name__ == "__main__":
    帮大家越来越好()
