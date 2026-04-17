package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Comment provided by vendor during NVD analysis.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VendorComment  {

  private String vendor;
  private String comment;
  private ZonedDateTime lastModifiedDate;

}