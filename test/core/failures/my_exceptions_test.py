
import pytest
import core.failures.MyExeptions as me

def test_creates_post_error_is_exception():
    with pytest.raises(me.CreatePostError) as ex:
        raise me.CreatePostError("hello")


@pytest.fixture
def exception_message():
    return {"id":20, "message":"not found"}

class TestIdNotFound:

    def test_it_is_exception(self,exception_message):
       with pytest.raises(me.IdNotFound):
         raise me.IdNotFound(exception_message)
    
    
    def test_returns_correct_message(self, exception_message):
        ex = me.IdNotFound(**exception_message)
        
        assert (str(ex) == "20 -> not found")