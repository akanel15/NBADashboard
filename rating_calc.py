def offensive_rating_calc(pts, ast, reb, fg_pct):
    MAX_PTS = 28
    MAX_AST = 8
    MAX_REB = 11
    MAX_FG = 0.5

    # pts worth 60%
    if pts >= MAX_PTS:
        pts_score = 1
    else:
        pts_score = pts/MAX_PTS

    
    # ast worth 15%
    if ast >= MAX_AST:
        ast_score = 1
    else:
        ast_score = ast/MAX_AST

    # reb worth 15%
    if reb >= MAX_REB:
        reb_score = 1
    else:
        reb_score = reb/MAX_REB
    
    # fg percentage worth 10%
    if fg_pct >= MAX_FG:
        fg_score = 1
    else:
        fg_score = fg_pct/MAX_FG

    off_factor = pts_score * 0.30 + ast_score * 0.075 + reb_score * 0.075 + fg_score * 0.05 + 0.5
    off_rating = off_factor * 100
    off_rating = round(off_rating)

    return off_rating
    
def defensive_rating_calc(stl, blk):
    # Calculated as an overall sum of both catigories to make fair
    MAX_STL = 1.3
    MAX_BLK = 1.3
    
    if stl >= MAX_STL:
        stl_score = 1
    else:
        stl_score = stl/MAX_STL

    if blk >= MAX_BLK:
        blk_score = 1
    else:
        blk_score = blk/MAX_BLK


    def_factor = blk_score * 0.25 + stl_score * 0.25 + 0.5
    def_rating = def_factor * 100
    def_rating = round(def_rating)

    return def_rating