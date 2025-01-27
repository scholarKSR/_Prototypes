# Impements the LifeGrid ADT for use with the game of Life.
from array import Array2D

class LifeGrid:
	# Defines conststns to represent the cell states
	DEAD_CELL = 0
	LIVE_CELL = 1
	
	# creates the game grid and initializes the cells to dead
	def __init__( self, numRows, numCols ):
		# Allocate a 2D array for the grid
		self._grid = Array2D( numRows, numCols )
		# Clear the grid and set all cellsto dead
		self.configure( list() )
		
	# returns the number of rows in the grid
	def numRows( self ):
		return self._grid.numRows()
	
	# returns the number of columns in the grid
	def numCols( self ):
		return self._grid.numCols()
		
	# Configure the grid to contain the given live cells
	def configure( self, coordList ):
		for i in range(numRows):
			for j in range( numCols ):
				self.clearCell(  i, j )
		
		# Set the indicated cells to be alive
		for coord in coordList:
			self.setCell( coord[0], coord[1] )
			
	# Does the indicated cell contain a live organism?
	def isLiveCell(self,row,col):
		return self._grid[row,col] == GameGrid.LIVE_CELL
	
	# Clears the indicated cell by setting it to dead
	def clearCell( self, row,col ):
		self._grid[row,col] = GameGrid.DEAD_CELL
	
	# Sets the indicated cell to be alive
	def setCell(self, row, col):
		self._grid[row,col] = GameGrid.LIVE_CELL
	
	# Returns the number of live neighbours for the giveb cell
	def numLiveNeighbour( self, row, col ):
		...
