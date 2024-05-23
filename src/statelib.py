from customLogic import AtomicStatement, ConditionalStatement, StatementList

class StatementFactory:
    precepts = [ 
        AtomicStatement("won_prev"),
        AtomicStatement("lost_prev"),
        AtomicStatement("has_won_before"),
        AtomicStatement("has_lost_before")
        AtomicStatement("on_3_winstreak_or_higher"),
        AtomicStatement("on_3_lossstreak_or_higher"),
        AtomicStatement("feeling_cautious"),
        AtomicStatement("feeling_unconstrained")
    ]

    personality = [
        AtomicStatement("agent_rational"), 
        AtomicStatement("agent_freespirited"), 
        AtomicStatement("agent_conservative"),
        AtomicStatement("agent_temperamental")
    ]

    internal_state = [
        ConditionalStatement("agent_feeling_lucky", [AtomicStatement("on_3_winstreak"),AtomicStatement("agent_freespirited")]),
        ConditionalStatement("agent_feeling_unlucky", [AtomicStatement("on_3_lossstreak"),AtomicStatement("agent_conservative")]),
        ConditionalStatement("agent_feeling_neutral", [AtomicStatement("won_prev"),]),
        ConditionalStatement("agent_feeling_cautious", [AtomicStatement("has_lost_before"), AtomicStatement("agent_temperamental")]),
        ConditionalStatement("agent_feeling_extra_cautious", [AtomicStatement("has_lost_before"), AtomicStatement("lost_prev"), AtomicStatement("agent_temperamental")]),
        ConditionalStatement("agent_total_shutdown", [ConditionalStatement("agent_feeling_extra_cautious"), AtomicStatement("on_3_lossstreak")]),
        ConditionalStatement("agent_feeling_unconstrained", [AtomicStatement("feeling_unconstrained"),])
    ]
    
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def initialize_agent_kb():
        statement_list = StatementList()
        for state in StatementFactory.internal_state:
            statement_list.add(state)
        return statement_list

    
