from evennia import default_cmds


class CmdBan(default_cmds.MuxCommand):
    """
       +Ban - Assigns bad luck to a character in a room..
    
       Usage: 
        +ban <args>
    
       Bad luck can be reginerated when you leave the room.
    
    """
    help_category = "Fate Magic"    # default
    auto_help = True             # default
    key = "+Ban"
    locks = "cmd:all()"

    def func(self):
        """confirms the target and initiates the search"""

        # save the target object onto the command
        # this will use Evennia's default multimatch handling if more than one object matches
        self.target = self.caller.search(self.lhs, global_search=True)
        self.target2 = self.caller.search(self.rhs, global_search=True)
        # initialize a list to store rooms we've visited
        self.caller.msg("target0: %s" % self.target)
        self.caller.msg("target2: %s" % self.target2)
        self.target.db.ban = self.target2
        
