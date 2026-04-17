package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Weakness row as presented on the NVD detail page.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NVDWeakness extends Weakness {

  private String source;

}