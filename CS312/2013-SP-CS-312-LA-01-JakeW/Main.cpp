#include <iostream>
using namespace std;

int main ()
{
	cout << "Hello World!" << "\n";
	return 0;
}

/// A test class.
/// A more detailed definition of what it is used for.
class Test
{
	public:
		/// An enum type.
		/// The documentation block cannot be put after the enum!
		enum EnumType
		{
			Monday,
			Tuesday
		};
		
		/// a member function.
		/// This can be used to alter/access data from within an instance of the Test class.
		void member();

	protected:
		/// An integer value.
		/// This integer will be used to store a value pertaining to the day of the week (for example.)
		int value;
};
