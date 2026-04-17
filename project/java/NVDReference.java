package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Reference URL with NVD resource tags.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NVDReference extends Reference {

  private List<String> resourceTags;

}