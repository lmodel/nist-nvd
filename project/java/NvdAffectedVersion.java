package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The status of one version of a product, or of a range of its versions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdAffectedVersion  {

  private String version;
  private String status;
  private String versionType;
  private String lessThan;
  private String lessThanOrEqual;
  private List<NvdVersionChange> changes;


}