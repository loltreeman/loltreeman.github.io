import pandas as pd
from RubiksCube2 import Cube2

# Load the scrambles and competitions data
scrambles = pd.read_csv("WCA_export_Scrambles.tsv", delimiter="\t")
competitions = pd.read_csv('WCA_export_Competitions.tsv', delimiter='\t')

rc = Cube2()

def findMovesScrambles(country: str, num_moves: int) -> list:
    # Filter 2x2 scrambles
    scrambles2x2 = scrambles[scrambles.eventId == "222"].reset_index(drop=True)

    # Get competition IDs for the specified country
    country_comps = competitions[competitions.countryId == country].id.tolist()

    comp_col = []
    round_type_col = []
    moves_scrambles = []
    group_id_col = []
    scramble_num_col = []

    for comp in country_comps:
        comp_scramble_table = scrambles2x2[scrambles2x2.competitionId == comp].reset_index(drop="index")

        for scr in comp_scramble_table.scramble:
            solution, _ = rc.solveKorf(num_moves, scr, findingdepth=False, finalphase=True)
            if solution is None:
                continue

            comp_col.append(comp)
            round_type_col.append(comp_scramble_table[comp_scramble_table.scramble == scr].iloc[0]['roundTypeId'])
            moves_scrambles.append(scr)
            group_id_col.append(comp_scramble_table[comp_scramble_table.scramble == scr].iloc[0]['groupId'])
            scramble_num_col.append(comp_scramble_table[comp_scramble_table.scramble == scr].iloc[0]['scrambleNum'])

    # Create a DataFrame and save it to a CSV file
    result_df = pd.DataFrame({
        "comp": comp_col,
        "roundTypeId": round_type_col,
        "scramble": moves_scrambles,
        "groupId": group_id_col,
        "scrambleNum": scramble_num_col
    })

    result_df.to_csv(f"official{num_moves}movescrambles_{country}.csv", index=False)

    return moves_scrambles

if __name__ == "__main__":
    country = input("Enter country: ")
    num_moves = int(input("Enter the number of moves: "))
    
    moves_scrambles = findMovesScrambles(country, num_moves)
    print(f"There have been {len(moves_scrambles)} {num_moves}-move official scrambles in {country}.")
